import './App.css';
import { useEffect } from "react";

const tg = window.Telegram.WebApp

function App() {
    useEffect(() => {
        tg.ready();
    }, []);

    const onClose = () => {

    }
    return (
        <div className="App">
            It works
            <button onClick={onClose}>Закрыть</button>
        </div>
    );
}

export default App;
