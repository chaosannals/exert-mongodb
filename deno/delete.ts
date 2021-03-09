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

// deleteOne
const deleteCount = await users.deleteOne({ _id: 1 });

console.log("deleteCount:", deleteCount);

// deleteMany
const deleteCount2 = await users.deleteMany({ username: "test" });

console.log("deleteCount2:", deleteCount2);
