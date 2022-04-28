package crud

import (
	"context"
	"log"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
)

func UpdateOneDemo(collection *mongo.Collection, ctx context.Context) {
	log.Println("======= update one =======")
	result, err := collection.UpdateOne(ctx, bson.M{
		"Name": "Pi",
	}, bson.D{
		bson.E{Key: "$set", Value: bson.D{
			bson.E{Key: "UpdateOne", Value: "1"},
			bson.E{Key: "status", Value: 213},
		}},
		bson.E{Key: "$currentDate", Value: bson.D{
			bson.E{Key: "lastModified", Value: true},
		}},
	})
	if err != nil {
		log.Fatalln(err)
	}
	log.Println(result)
}

func UpdateManyDemo(collection *mongo.Collection, ctx context.Context) {
	log.Println("======= update many =======")
	result, err := collection.UpdateMany(ctx, bson.M{
		"Name": bson.M{
			"$regex": `value-\d+1`,
		},
	}, bson.D{
		bson.E{Key: "$set", Value: bson.D{
			bson.E{Key: "UpdateMany", Value: 100},
			bson.E{Key: "status", Value: 1},
		}},
		bson.E{Key: "$currentDate", Value: bson.D{
			bson.E{Key: "lastModified", Value: true},
		}},
	})
	if err != nil {
		log.Fatalln(err)
	}
	log.Println(result)
}
