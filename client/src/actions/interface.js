import axios from 'axios'

export const loadLocations = async () => {
  try {
    const locations = await axios.get('/locations');
    return locations;
  } catch(err) {
    console.error(err.message);
  }
}
