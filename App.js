import Discourse from 'discourse-js';

const userApiKey = '<user-api-key-from-discourse>'; //get this from CJ
const apiUsername = '<user-username-from-discourse>';
const baseUrl = '<your-discourse-url>' || 'http://localhost:3000';

const discourse = new Discourse();
discourse.config({ userApiKey, apiUsername, baseUrl })

discourse.posts
    .create({
        topic_id: 11, // optional (required for creating a new post on a topic.)
        raw: 'Hello World',
        imageUri: imageUri, // optional to create a post/topic with an image.
    })
    .then(res => console.log(res))
    .catch(err => console.log(err));
