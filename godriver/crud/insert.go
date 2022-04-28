package crud

import (
	"context"
	"fmt"
	"log"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
)

func InsertOneDemo(collection *mongo.Collection, ctx context.Context) {
	log.Println("======= insert one ========")
	res, err := collection.InsertOne(ctx, bson.D{
		bson.E{Key: "Name", Value: "Pi"},
		bson.E{Key: "Value", Value: 3.1415},
	})
	if err != nil {
		panic(err)
	}
	fmt.Println(res.InsertedID)
}

func InsertManyDemo(collection *mongo.Collection, ctx context.Context) {
	log.Println("======= insert many ==========")
	others := make([]interface{}, 100)
	for i := 0; i < 100; i++ {
		others[i] = bson.D{
			bson.E{Key: "Name", Value: fmt.Sprintf("value-%d", i)},
			bson.E{Key: "Value", Value: i + 10000},
		}
	}
	collection.InsertMany(ctx, others)
}
