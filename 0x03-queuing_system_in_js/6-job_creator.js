const kue = require('kue');
const queue = kue.createQueue();
const jobData = {
  phoneNumber: string,
  message: string,
};
for (let i = 1; i <= jobData.lenghth; i++) {
  queue.create("push_notification_code", {data: i})
  .save();
};
