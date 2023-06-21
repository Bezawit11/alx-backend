const r = require('redis')
const redisClient = r.createClient()
(async () => {
    await redisClient.connect();
})();
redisClient.on('ready', () => {
    console.log("Redis client connected to the server");
});
redisClient.on('error', (err) => {
    console.error("Redis client not connected to the server: ${err}");
});
