import { Bson, MongoClient } from "https://deno.land/x/mongo@v0.21.0/mod.ts";

// Defining schema interface
interface UserSchema {
  _id: { $oid: string };
  username: string;
  password: string;
}

const client = new MongoClient();
await client.connect("mongodb://localhost:27017");

const db = client.database("test");
const users = db.collection<UserSchema>("users");

// findOne
const user1 = await users.findOne({ _id: 1 });

console.log("user1", user1);

// find
const all_users = await users.find({ username: { $ne: null } });

console.log("all_users:", all_users);

// find by ObjectId
const user1_id = await users.findOne({
  _id: new Bson.ObjectId("604710422982090eb7210116"),
});

console.log("user1_id", user1_id);

// count
const count = await users.count({ username: { $ne: null } });

console.log("count:", count);

// aggregation
const docs = await users.aggregate([
  { $match: { username: "many" } },
  { $group: { _id: "$username", total: { $sum: 1 } } },
]);

console.log("docs:", docs);

// Skip
const skipTwo = await users.find().skip(2);

console.log("skipTwo:", skipTwo);

// Limit
const featuredUser = await users.find().limit(5);

console.log("featuredUser:", featuredUser);