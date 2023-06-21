const redis = require('redis');
const redisClient = redis.createClient();
redisClient.on('ready', () => {
    console.log("Redis client connected to the server");
});
redisClient.on('error', (err) => {
    console.error("Redis client not connected to the server: ${err}");
});
const setNewSchool = (schoolName, value) => {
  redisClient.SET(schoolName, value);
};
const displaySchoolValue = (schoolName) => {
  console.log(redisClient.GET(schoolName));
};

redisClient.hmset("HolbertonSchools",
		   "Portland", 50,
		   "Seattle", 80,
		   "New York", 20,
		   "Bogota", 20,
	 	   "Cali", 40,
		   "Paris", 2)
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
