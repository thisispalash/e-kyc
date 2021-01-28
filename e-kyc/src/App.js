import './main.css';

import { HostEnter, LinkGen } from './start.js';
import { DocUpload, DataUpload } from './document.js';
import { VerifyFace, AllDone } from './face.js';
import './storage.js';


function App() {
  // return (<LinkGen />);
  // return (<DocUpload />);
  // return (<DataUpload />);
  // return (<VerifyFace />);
  return (<AllDone />);
}

export default App;