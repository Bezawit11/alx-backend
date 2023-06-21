const redis = require('redis');
const publisher = redis.createClient();
publisher.on('ready', () => {
    console.log("Redis client connected to the server");
});
publisher.on('error', (err) => {
    console.error("Redis client not connected to the server:", err);
});
const greet = () => {
  console.log("About to send MESSAGE");
};
const publishMessage = (message, time) => {
  setTimeout(greet, time);
  publisher.connect();
  publisher.publish('holberton school channel', JSON.stringify(message));
};
