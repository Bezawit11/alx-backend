const redis = require('redis');
const redisClient = redis.createClient();
redisClient.on('ready', () => {
    console.log("Redis client connected to the server");
});
redisClient.on('error', (err) => {
    console.error("Redis client not connected to the server: ${err}");
});

redisClient.HMSET("HolbertonSchools",
		   "Portland", 50,
		   "Seattle", 80,
		   "New York", 20,
		   "Bogota", 20,
	 	   "Cali", 40,
		   "Paris", 2)
const result = redisClient.HGET("HolbertonSchools", "Portland");
console.log(result);
