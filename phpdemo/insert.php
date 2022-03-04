<?php

require 'vendor/autoload.php';

use MongoDB\Client;

$client = new Client('mongodb://root:root@localhost:27017/?authSource=admin&authMechanism=SCRAM-SHA-256&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false');
$collection = $client->test->testers;

$insertOneResult = $collection->insertOne([
    'testname' => 'ttt123123',
    'testno' => 123,
]);

var_export($insertOneResult->getInsertedCount());
echo PHP_EOL;
var_export($insertOneResult->getInsertedId());


echo PHP_EOL.'=========================================='.PHP_EOL;


$testers = [];
$t = time();
for($i = 0; $i < 1000; ++$i) {
    $testers[] = [
        'testname' => "tttt{$i}n",
        "testno" => $t + $i,
        'is_many' => true,
    ];
}
$insertManyResult = $collection->insertMany($testers);

var_export($insertManyResult->getInsertedCount());
echo PHP_EOL;
var_export($insertManyResult->getInsertedIds());
