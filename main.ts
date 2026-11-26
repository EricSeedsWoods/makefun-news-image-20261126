import { existsSync, mkdirSync, copyFileSync, statSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, resolve } from 'node:path';

/**
 * make.fun news-image-20261126 delivery pipeline
 * Transfers the synthesized daily news infographic to the designated evaluation volume.
 */
function deliverEntry(): void {
  const currentDirectory = dirname(fileURLToPath(import.meta.url));
  const sourceImage = resolve(currentDirectory, 'entry.png');
  const destinationDirectory = process.env.MAKEFUN_OUTPUT_DIR || '/output';
  const targetImage = resolve(destinationDirectory, 'entry.png');

  if (!existsSync(sourceImage)) {
    throw new Error(`[news-image-pipeline] Source artifact not found: ${sourceImage}`);
  }

  const fileStats = statSync(sourceImage);
  if (fileStats.size === 0) {
    throw new Error(`[news-image-pipeline] Source artifact is empty: ${sourceImage}`);
  }

  if (!existsSync(destinationDirectory)) {
    mkdirSync(destinationDirectory, { recursive: true });
  }

  copyFileSync(sourceImage, targetImage);
  console.log(`[news-image-pipeline] Delivered entry.png (${(fileStats.size / 1024).toFixed(1)} KiB) -> ${targetImage}`);
}

deliverEntry();
