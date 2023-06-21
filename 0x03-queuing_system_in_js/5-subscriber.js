const redis = require('redis');
const redisClient = redis.createClient();
redisClient.on('ready', () => {
    console.log("Redis client connected to the server");
});
redisClient.on('error', (err) => {
    console.error("Redis client not connected to the server: ${err}");
});
redisClient.on(“message”, function ("holberton school channel", message) {
 console.log(message);
});
redisClient.subscribe(“notification”);
