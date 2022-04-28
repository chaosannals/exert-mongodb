package crud

import (
	"context"
	"log"

	// "regexp"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
)

func RemoveOneDemo(collection *mongo.Collection, ctx context.Context) {
	log.Println("======= remove one =======")
	result, err := collection.DeleteOne(ctx, bson.M{
		"Name": bson.M{"$regex": `value-\d2`},
	})
	if err != nil {
		log.Fatalln(err)
	}
	log.Println(result)
}

func RemoveManyDemo(collection *mongo.Collection, ctx context.Context) {
	log.Println("======= remove many =======")
	result, err := collection.DeleteMany(ctx, bson.M{
		"Name": bson.M{"$regex": `value-\d7`},
	})
	if err != nil {
		log.Fatalln(err)
	}
	log.Println(result)
}