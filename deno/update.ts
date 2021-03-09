import { Bson, MongoClient } from "https://deno.land/x/mongo@v0.21.0/mod.ts";

const client = new MongoClient();
await client.connect("mongodb://localhost:27017");

// Defining schema interface
interface UserSchema {
  _id: { $oid: string };
  username: string;
  password: string;
}

const db = client.database("test");
const users = db.collection<UserSchema>("users");

// updateOne
const a = await users.updateOne(
  { username: { $ne: null } },
  { $set: { username: "USERNAME" } },
);

console.log('a: ', a);

// updateMany
const b = await users.updateMany(
  { username: { $ne: null } },
  { $set: { username: "USERNAME" } },
);

console.log('b: ', b);