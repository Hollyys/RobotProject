import image from './knu.png'
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={image} width = '800px' />
        <p>
          모바일 로봇 프로그래밍 중간과제
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
