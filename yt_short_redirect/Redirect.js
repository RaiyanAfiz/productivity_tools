const { origin, pathname } = location;
console.log(location);
const newURL = `${origin}${pathname.replace("shorts/", "watch?v=")}`;
location.replace(newURL);
