const redis = require('redis');
const publisher = redis.createClient();
publisher.on('ready', () => {
    console.log("Redis client connected to the server");
});
publisher.on('error', (err) => {
    console.error("Redis client not connected to the server: ${err}");
});
(async () => {

  const article = {
    id: '123456',
    name: 'Using Redis Pub/Sub with Node.js',
    blog: 'Logrocket Blog',
  };

  await publisher.connect();

  await publisher.publish('article', JSON.stringify(article));
})();
