// import logo from './logo.svg';
import './App.css';
import { useState, useEffect } from 'react';
import axios from 'axios';

// const LIST_BLOG = [
//   {
//     "name": "Blog 1",
//     "content": "Content Blog 1",
//   },
//   {
//     "name": "Blog 2",
//     "content": "Content Blog 2",
//   }
// ]

function App() {
  const [list_blog, setListBLog] = useState([])

  useEffect(() => {
    axios
      .get('http://127.0.0.1:8001/api/blog')
      .then(res => {
        setListBLog(res.data)
      })
      .catch(err => {
        console.log(err)
      })
  }, [])

  return (
    <div >
      {
        list_blog.map(blog => (
          <div>
            <div>{blog.title}</div>
            <div>{blog.content}</div>
          </div>
        ))
      }
    </div>
  );
}

export default App;

