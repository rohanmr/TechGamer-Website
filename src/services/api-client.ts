import axios from "axios";

export default axios.create({
  baseURL: "https://api.rawg.io/api",
  params: {
    key: "cd99c6022238450e8a6e9f78160a03b5",
  },
});
