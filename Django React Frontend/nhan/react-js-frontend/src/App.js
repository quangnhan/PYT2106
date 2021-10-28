import logo from './logo.svg';
import './App.css';

const list_blog = [
  {
    "name": "Blog 1",
    "content": "Content BLog 1",
  },
  {
    "name": "Blog 2",
    "content": "Content BLog 2",
  }
]

function App() {
  return (
    <div >
      {
        list_blog.map(blog => (
          <div>
            <div>{blog.name}</div>
            <div>{blog.content}</div>
          </div>
        ))
      }
    </div>
  );
}

export default App;
