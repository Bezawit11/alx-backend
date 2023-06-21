const kue = require('kue');
const queue = kue.createQueue();
const jobData = {
  phoneNumber: string,
  message: string,
};
queue
        .create("push_notification_code", jobData)
        .save((err) => {
            if (err) {
                console.error("Notification job completed");
                done(err);
            }
            if (!err) {
                console.log("Notification job failed");
                done();
            }
        });
