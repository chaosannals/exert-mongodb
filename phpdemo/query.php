<?php


require 'vendor/autoload.php';

use MongoDB\Client;

$client = new Client('mongodb://root:root@localhost:27017/?authSource=admin&authMechanism=SCRAM-SHA-256&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false');
$collection = $client->test->testers;

$one = $collection->findOne([
    'testno' => ['$lte' => 123 ],
]);

var_export($one);

echo PHP_EOL.'=========================================='.PHP_EOL;

$many = $collection->find([
    'testno' => ['$gt' => 123 ],
    'is_many' => true,
    'testname' => ['$regex' => 'tttt1\\d+n'],
], [
    'limit' => 3,
    'skip' => 2,
    'projection' => [
        'is_many' => 0,
    ],
]);

foreach($many as $i) {
    var_export($i);
}