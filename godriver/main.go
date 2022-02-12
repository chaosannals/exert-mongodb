package main

import (
	"context"
	"fmt"
	"log"
	"time"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
	"go.mongodb.org/mongo-driver/mongo/readpref"
)

func main() {
	ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
	defer cancel()
	client, err := mongo.Connect(ctx, options.Client().ApplyURI("mongodb://localhost:27017"))
	if err != nil {
		panic(err)
	}
	defer func() {
		if e := client.Disconnect(ctx); e != nil {
			panic(e)
		}
	}()
	err = client.Ping(ctx, readpref.Primary())
	if err != nil {
		panic(err)
	}
	collection := client.Database("testing").Collection("tester")
	res, err := collection.InsertOne(ctx, bson.D{
		bson.E{Key: "Name", Value: "Pi"},
		bson.E{Key: "Value", Value: 3.1415},
	})
	if err != nil {
		panic(err)
	}
	fmt.Println(res.InsertedID)
	others := make([]interface{}, 100)
	for i := 0; i < 100; i++ {
		others[i] = bson.D {
			bson.E{Key: "Name", Value: fmt.Sprintf("value-%d", i), },
			bson.E{Key: "Value", Value: i + 10000, },
		}
	}
	collection.InsertMany(ctx, others)

	cur, err := collection.Find(ctx, bson.D{})
	if err != nil {
		panic(err)
	}
	defer cur.Close(ctx)
	for cur.Next(ctx) {
		var r bson.D
		err := cur.Decode(&r)
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println(r)
	}
	if err := cur.Err(); err != nil {
		log.Fatal(err)
	}
}
