6KSFx- Procedural Audio Dataset
Procedural audio—generating sound from scratch using computational processes—offers a powerful approach to creating sound effects, often referred to as digital Foley. However, research and optimization in this field have been hindered by the limited availability of publicly accessible samples and models.

This dataset addresses that gap by providing 6,000 synthetic audio samples to advance research in sound synthesis. With 30 categories containing 100 samples each, this 2.56 GB dataset supports the development of new synthesis techniques and evaluation methods. By making these samples publicly available, we aim to empower researchers, audio developers, and sound designers to optimize and expand procedural audio applications.

Additionally, 50 noise-augmented samples have been included for machine learning applications.

Each sample follows the naming format: [Sound Category] - [Sample Number] - [Label]
| Category          | Label | Category          | Label | Category          | Label | Category          | Label |
|------------------|-------|------------------|-------|------------------|-------|------------------|-------|
| Applause        | 1     | Gunshots         | 19    | Whoosh          | 38    | Twang           | 56    |
| Church Bells    | 3     | Helicopter       | 21    | Fireworks       | 40    | Bounce Rubber   | 58    |
| Bubbles        | 5     | Pouring Hot Water | 23    | Concrete Footsteps | 42  | Electric Buzz   | 60    |
| Droplets       | 7     | Rain             | 25    | Wood Footsteps  | 44    |                  |       |
| Crackling      | 9     | Thunder          | 27    | Space Cannon    | 46    |                  |       |
| Debris Glass   | 11    | Waves            | 29    | Spray           | 48    |                  |       |
| Engine        | 13    | Wind             | 31    | Metal Debris    | 50    |                  |       |
| Explosions    | 15    | Boat             | 33    | Rocket          | 52    |                  |       |
| Fire          | 17    | Jet              | 35    | Concrete Debris | 54    |                  |       |

 The dataset is available for download in Zenodo: https://zenodo.org/records/14517916
 Paper of the Dateset: https://arxiv.org/abs/2501.17198

 In Github you will find the scripts for trimming, down-mixing, and labeling sound samples in the dataset, designed for streamlined audio processing and analysis.
