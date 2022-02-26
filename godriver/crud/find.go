package crud

import (
	"context"
	"fmt"
	"log"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
)

func FindDemo(collection *mongo.Collection, ctx context.Context) {
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