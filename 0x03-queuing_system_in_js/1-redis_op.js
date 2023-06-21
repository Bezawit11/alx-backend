const redis = require('redis');
const redisClient = redis.createClient();
redisClient.on('ready', () => {
    console.log("Redis client connected to the server");
});
redisClient.on('error', (err) => {
    console.error("Redis client not connected to the server: ${err}");
});
function setNewSchool(schoolName, value) {
  redisClient.set(schoolName, value, function (err, res) {
  });
};
function displaySchoolValue(schoolName) {
  console.log(redisClient.get(schoolName));
};



displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
