package main

import (
	"context"
	"log"
	"time"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
	"go.mongodb.org/mongo-driver/mongo/readpref"
	"github.com/chaosannals/exert-mongodb-godriver/crud"
)

func main() {
	ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
	defer cancel()
	client, err := mongo.Connect(ctx, options.Client().ApplyURI("mongodb://localhost:27017").SetAuth(options.Credential{
		AuthMechanism: "SCRAM-SHA-256",
		Username: "root",
		Password: "root",
	}).SetDirect(true))
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
	log.Println("pong")
	collection := client.Database("testing").Collection("tester")
	crud.InsertOneDemo(collection, ctx)
	crud.InsertManyDemo(collection, ctx)
	crud.FindDemo(collection, ctx)
}
