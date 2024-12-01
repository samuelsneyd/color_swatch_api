import * as React from 'react';
import './App.css';

const API_ENDPOINT = 'http://127.0.0.1:8000';

type ColorSwatch = {
  type: 'rgb' | 'hsl';
} & Record<string, any>;

type RGBColorSwatch = {
  type: 'rbg';
  red: number;
  green: number;
  blue: number;
}

type HSLColorSwatch = {
  type: 'hsl';
  hue: number;
  saturation: number;
  lightness: number;
}

interface ColorSwatchProps extends React.HTMLAttributes<HTMLDivElement> {
  nColors?: number;
}

const fetchColors = async ({ nColors }: { nColors?: number } = {}): Promise<ColorSwatch[]> => {
  const url = new URL('/api/colors', API_ENDPOINT);
  if (nColors) {
    url.searchParams.append('n', nColors.toString());
  }
  try {
    return await fetch(url).then(res => res.json());
  } catch (e) {
    console.error(e);
    return [];
  }
};

const ColorBox = ({ colorSwatch, ...props }: { colorSwatch: ColorSwatch } & React.HTMLAttributes<HTMLDivElement>) => {
  let backgroundColor: string | undefined;

  switch (colorSwatch.type) {
    case 'rgb': {
      const swatch = colorSwatch as RGBColorSwatch;
      backgroundColor = '#' + [swatch.red, swatch.green, swatch.blue]
        .map(n => n.toString(16).padStart(2, '0'))
        .join('');
      break;
    }
    case 'hsl': {
      const swatch = colorSwatch as HSLColorSwatch;
      backgroundColor = `hsl(${swatch.hue} ${swatch.saturation}% ${swatch.lightness}%)`;
      break;
    }
  }

  return (
    <div className="colorBox" style={{ backgroundColor }} {...props}>
      <p className="shadow-text">{backgroundColor}</p>
    </div>
  );
};


const ColorSwatch = ({ nColors = 5, ...props }: ColorSwatchProps) => {
  const [colors, setColors] = React.useState<ColorSwatch[]>([]);

  React.useEffect(() => {
    fetchColors({ nColors }).then(setColors);
  }, []);

  return (
    <>
      <div className="container" {...props}>
        {colors.map((colorSwatch, index) => (
          <ColorBox key={index} colorSwatch={colorSwatch} />
        ))}
      </div>
      <button onClick={() => fetchColors().then(setColors)}>
        New colors
      </button>
    </>
  );
};


function App() {
  return (
    <>
      <h1>Color Swatch</h1>
      <ColorSwatch />
    </>
  );
}

export default App;
