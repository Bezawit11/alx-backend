const redis = require('redis');
const redisClient = redis.createClient();
redisClient.on('ready', () => {
    console.log("Redis client connected to the server");
});
redisClient.on('error', (err) => {
    console.error("Redis client not connected to the server: ${err}");
});
const setNewSchool(schoolName, value) {
  redisClient.SET(schoolName, value, function (err, res) {
  });
};
const displaySchoolValue(schoolName) {
  console.log(redisClient.GET(schoolName));
};



displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
