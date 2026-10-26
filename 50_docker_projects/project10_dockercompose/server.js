const express = require('express');
const redis = require('redis');

const app = express();

// Connect to the Redis container using its service name as the hostname
const client = redis.createClient({
  url: 'redis://redis-cache:6379'
});

client.connect().catch(console.error);

app.get('/', async (req, res) => {
  try {
    let views = await client.incr('page_views');
    res.send(`🚀 Docker Compose Stack Online! Total Page Views: ${views}`);
  } catch (err) {
    res.send('🚀 Docker Compose Stack Online! (Connecting to Redis...)');
  }
});

app.listen(3000, () => console.log('Web service listening on port 3000'));
