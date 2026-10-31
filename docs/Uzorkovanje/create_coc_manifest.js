const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, 
        Header, Footer, AlignmentType, HeadingLevel, BorderStyle, WidthType, 
        ShadingType, PageNumber, VerticalAlign } = require('docx');
const fs = require('fs');

const border = { style: BorderStyle.SINGLE, size: 1, color: "000000" };
const borders = { top: border, bottom: border, left: border, right: border };
const thickBorder = { style: BorderStyle.SINGLE, size: 12, color: "1F4E79" };
const thickBorders = { top: thickBorder, bottom: thickBorder, left: thickBorder, right: thickBorder };

function cell(text, opts = {}) {
  return new TableCell({
    borders,
    width: { size: opts.width || 2000, type: WidthType.DXA },
    shading: opts.shading ? { type: ShadingType.CLEAR, fill: opts.shading } : undefined,
    verticalAlign: VerticalAlign.CENTER,
    margins: { top: 40, bottom: 40, left: 60, right: 60 },
    children: [new Paragraph({
      alignment: opts.align || AlignmentType.LEFT,
      children: [new TextRun({ text: text || "", size: opts.size || 18, bold: opts.bold || false })]
    })]
  });
}

function emptyCell(width) {
  return new TableCell({
    borders,
    width: { size: width || 2000, type: WidthType.DXA },
    margins: { top: 40, bottom: 40, left: 60, right: 60 },
    children: [new Paragraph({ children: [new TextRun({ text: " ", size: 18 })] })]
  });
}

// ========== CHAIN OF CUSTODY ==========
const cocDoc = new Document({
  styles: {
    default: { document: { run: { font: "Arial", size: 20 } } }
  },
  sections: [{
    properties: {
      page: {
        size: { width: 11906, height: 16838 },
        margin: { top: 720, right: 720, bottom: 720, left: 720 }
      }
    },
    children: [
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { after: 60 },
        children: [new TextRun({ text: "CHAIN OF CUSTODY / LANAC DOKAZA", size: 28, bold: true, color: "1F4E79" })]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { after: 200 },
        children: [new TextRun({ text: "Obrazac po uzorku — ispunjava se na terenu", size: 18, italics: true })]
      }),

      // Header info
      new Table({
        width: { size: 10466, type: WidthType.DXA },
        columnWidths: [2616, 2617, 2616, 2617],
        rows: [
          new TableRow({ children: [
            cell("Broj uzorka:", { width: 2616, bold: true, shading: "D6E3F0" }),
            emptyCell(2617),
            cell("Datum:", { width: 2616, bold: true, shading: "D6E3F0" }),
            emptyCell(2617),
          ]}),
          new TableRow({ children: [
            cell("Vrijeme (početak):", { width: 2616, bold: true, shading: "D6E3F0" }),
            emptyCell(2617),
            cell("Vrijeme (kraj):", { width: 2616, bold: true, shading: "D6E3F0" }),
            emptyCell(2617),
          ]}),
          new TableRow({ children: [
            cell("GPS koordinate:", { width: 2616, bold: true, shading: "D6E3F0" }),
            emptyCell(2617),
            cell("Lokacija (opis):", { width: 2616, bold: true, shading: "D6E3F0" }),
            emptyCell(2617),
          ]}),
        ]
      }),

      new Paragraph({ spacing: { before: 200 }, children: [new TextRun({ text: "VRSTA UZORKA I METODA", size: 20, bold: true, color: "1F4E79" })] }),
      new Table({
        width: { size: 10466, type: WidthType.DXA },
        columnWidths: [2616, 7850],
        rows: [
          new TableRow({ children: [
            cell("Matrica:", { width: 2616, bold: true, shading: "D6E3F0" }),
            cell("☐ Voda (slatka)   ☐ Morska voda   ☐ Sediment   ☐ Tlo 0–10 cm   ☐ Tlo 10–30 cm   ☐ Prašina   ☐ Zrak (pasivni)   ☐ Ostalo: ________", { width: 7850, size: 16 }),
          ]}),
          new TableRow({ children: [
            cell("Dubina / Visina:", { width: 2616, bold: true, shading: "D6E3F0" }),
            emptyCell(7850),
          ]}),
          new TableRow({ children: [
            cell("Metoda uzorkovanja:", { width: 2616, bold: true, shading: "D6E3F0" }),
            emptyCell(7850),
          ]}),
          new TableRow({ children: [
            cell("Tražene analize:", { width: 2616, bold: true, shading: "D6E3F0" }),
            cell("☐ Teški metali   ☐ VOC   ☐ Halogenidi   ☐ PCDD/F   ☐ Ostalo: ________________", { width: 7850, size: 16 }),
          ]}),
        ]
      }),

      new Paragraph({ spacing: { before: 200 }, children: [new TextRun({ text: "FOTO / VIDEO DOKUMENTACIJA", size: 20, bold: true, color: "1F4E79" })] }),
      new Table({
        width: { size: 10466, type: WidthType.DXA },
        columnWidths: [2616, 2617, 2616, 2617],
        rows: [
          new TableRow({ children: [
            cell("Hash foto mjesta:", { width: 2616, bold: true, shading: "D6E3F0" }),
            emptyCell(2617),
            cell("Hash foto uzorka:", { width: 2616, bold: true, shading: "D6E3F0" }),
            emptyCell(2617),
          ]}),
          new TableRow({ children: [
            cell("Video snimka (da/ne):", { width: 2616, bold: true, shading: "D6E3F0" }),
            emptyCell(2617),
            cell("Cloud link / ID:", { width: 2616, bold: true, shading: "D6E3F0" }),
            emptyCell(2617),
          ]}),
        ]
      }),

      new Paragraph({ spacing: { before: 200 }, children: [new TextRun({ text: "OSOBE", size: 20, bold: true, color: "1F4E79" })] }),
      new Table({
        width: { size: 10466, type: WidthType.DXA },
        columnWidths: [2616, 2617, 2616, 2617],
        rows: [
          new TableRow({ children: [
            cell("Uzorkovatelj (ime):", { width: 2616, bold: true, shading: "D6E3F0" }),
            emptyCell(2617),
            cell("Potpis:", { width: 2616, bold: true, shading: "D6E3F0" }),
            emptyCell(2617),
          ]}),
          new TableRow({ children: [
            cell("Svjedok (ime):", { width: 2616, bold: true, shading: "D6E3F0" }),
            emptyCell(2617),
            cell("Potpis:", { width: 2616, bold: true, shading: "D6E3F0" }),
            emptyCell(2617),
          ]}),
        ]
      }),

      new Paragraph({ spacing: { before: 200 }, children: [new TextRun({ text: "PRIJENOS U LABORATORIJ", size: 20, bold: true, color: "1F4E79" })] }),
      new Table({
        width: { size: 10466, type: WidthType.DXA },
        columnWidths: [2616, 2617, 2616, 2617],
        rows: [
          new TableRow({ children: [
            cell("Laboratorij:", { width: 2616, bold: true, shading: "D6E3F0" }),
            emptyCell(2617),
            cell("Datum predaje:", { width: 2616, bold: true, shading: "D6E3F0" }),
            emptyCell(2617),
          ]}),
          new TableRow({ children: [
            cell("Kurir / način:", { width: 2616, bold: true, shading: "D6E3F0" }),
            emptyCell(2617),
            cell("Broj pošiljke:", { width: 2616, bold: true, shading: "D6E3F0" }),
            emptyCell(2617),
          ]}),
          new TableRow({ children: [
            cell("Primatelj (lab):", { width: 2616, bold: true, shading: "D6E3F0" }),
            emptyCell(2617),
            cell("Potpis lab:", { width: 2616, bold: true, shading: "D6E3F0" }),
            emptyCell(2617),
          ]}),
        ]
      }),

      new Paragraph({ spacing: { before: 200 }, children: [new TextRun({ text: "NAPOMENE / INCIDENTI", size: 20, bold: true, color: "1F4E79" })] }),
      new Table({
        width: { size: 10466, type: WidthType.DXA },
        columnWidths: [10466],
        rows: [
          new TableRow({ children: [
            new TableCell({
              borders,
              width: { size: 10466, type: WidthType.DXA },
              margins: { top: 60, bottom: 60, left: 60, right: 60 },
              children: [
                new Paragraph({ children: [new TextRun({ text: " ", size: 18 })] }),
                new Paragraph({ children: [new TextRun({ text: " ", size: 18 })] }),
                new Paragraph({ children: [new TextRun({ text: " ", size: 18 })] }),
                new Paragraph({ children: [new TextRun({ text: " ", size: 18 })] }),
              ]
            })
          ]}),
        ]
      }),

      new Paragraph({
        spacing: { before: 300 },
        alignment: AlignmentType.CENTER,
        children: [new TextRun({ text: "Načelo: Svaki uzorak koji ne može na sud — nije uzorak, nego trošak.", size: 16, italics: true, color: "666666" })]
      }),
    ]
  }]
});

// ========== MANIFEST ==========
const manifestDoc = new Document({
  styles: {
    default: { document: { run: { font: "Arial", size: 18 } } }
  },
  sections: [{
    properties: {
      page: {
        size: { width: 16838, height: 11906 }, // Landscape A4
        margin: { top: 720, right: 720, bottom: 720, left: 720 }
      }
    },
    children: [
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { after: 100 },
        children: [new TextRun({ text: "MANIFEST UZORAKA — TERENSKI DAN", size: 26, bold: true, color: "1F4E79" })]
      }),
      new Paragraph({
        spacing: { after: 150 },
        children: [
          new TextRun({ text: "Datum terena: ______________    ", size: 18 }),
          new TextRun({ text: "Tim: ______________    ", size: 18 }),
          new TextRun({ text: "Koordinator: ______________", size: 18 })
        ]
      }),

      new Table({
        width: { size: 15398, type: WidthType.DXA },
        columnWidths: [1200, 1400, 1800, 1600, 1400, 1600, 1600, 1400, 1400, 1598],
        rows: [
          // Header
          new TableRow({
            children: [
              ["Br. uzorka", 1200], ["Vrijeme", 1400], ["Lokacija / GPS", 1800], ["Matrica", 1600],
              ["Dubina", 1400], ["Analize", 1600], ["Hash foto", 1600], ["Laboratorij", 1400],
              ["Datum slanja", 1400], ["Napomena", 1598]
            ].map(([text, w]) => new TableCell({
              borders,
              width: { size: w, type: WidthType.DXA },
              shading: { type: ShadingType.CLEAR, fill: "1F4E79" },
              verticalAlign: VerticalAlign.CENTER,
              margins: { top: 30, bottom: 30, left: 40, right: 40 },
              children: [new Paragraph({
                alignment: AlignmentType.CENTER,
                children: [new TextRun({ text, size: 14, bold: true, color: "FFFFFF" })]
              })]
            }))
          }),
          // Empty rows
          ...Array.from({ length: 12 }, () => new TableRow({
            children: [
              emptyCell(1200), emptyCell(1400), emptyCell(1800), emptyCell(1600),
              emptyCell(1400), emptyCell(1600), emptyCell(1600), emptyCell(1400),
              emptyCell(1400), emptyCell(1598)
            ]
          }))
        ]
      }),

      new Paragraph({
        spacing: { before: 200 },
        children: [new TextRun({ text: "Upute: ", bold: true, size: 16 }),
          new TextRun({ text: "Svaki red = jedan uzorak. Hash se upisuje odmah na terenu. Na kraju dana kopija ide koordinatorici + nositelju dosjea. Original ostaje u dosjeu tima.", size: 16 })]
      }),
      new Paragraph({
        spacing: { before: 80 },
        children: [new TextRun({ text: "Potpis voditelja tima: ________________________     Datum: ______________", size: 16 })]
      }),
    ]
  }]
});

Promise.all([
  Packer.toBuffer(cocDoc).then(b => fs.writeFileSync("/home/workdir/artifacts/Chain_of_Custody_Obrazac.docx", b)),
  Packer.toBuffer(manifestDoc).then(b => fs.writeFileSync("/home/workdir/artifacts/Manifest_Uzoraka_Predlozak.docx", b))
]).then(() => console.log("CoC + Manifest created successfully"));
