const express = require('express');
const app = express();
app.get('/', (req, res) => res.send('🚀 NodeJS API is running perfectly in Docker!'));
app.listen(3000, () => console.log('Server ready on port 3000'));
