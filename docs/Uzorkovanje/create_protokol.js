const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, 
        Header, Footer, AlignmentType, HeadingLevel, BorderStyle, WidthType, 
        ShadingType, PageNumber, LevelFormat } = require('docx');
const fs = require('fs');

const border = { style: BorderStyle.SINGLE, size: 1, color: "000000" };
const borders = { top: border, bottom: border, left: border, right: border };
const noBorder = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const noBorders = { top: noBorder, bottom: noBorder, left: noBorder, right: noBorder };

const doc = new Document({
  styles: {
    default: { document: { run: { font: "Arial", size: 22 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickStyle: true,
        paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 0 },
        run: { font: "Arial", size: 28, bold: true, color: "1F4E79" } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickStyle: true,
        paragraph: { spacing: { before: 200, after: 100 }, outlineLevel: 1 },
        run: { font: "Arial", size: 24, bold: true, color: "2E75B6" } },
      { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickStyle: true,
        paragraph: { spacing: { before: 160, after: 80 }, outlineLevel: 2 },
        run: { font: "Arial", size: 22, bold: true, color: "5B9BD5" } },
    ]
  },
  numbering: {
    config: [
      { reference: "bullets",
        levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
      { reference: "numbers",
        levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
    ]
  },
  sections: [{
    properties: {
      page: {
        size: { width: 11906, height: 16838 },
        margin: { top: 1134, right: 1134, bottom: 1134, left: 1134 }
      }
    },
    headers: {
      default: new Header({
        children: [new Paragraph({
          children: [
            new TextRun({ text: "PROTOKOL UZORKOVANJA — TERENSKI TIM", size: 18, bold: true, color: "1F4E79" }),
            new TextRun({ text: "  |  INTERNO — verzija 2.1 (korigirano)", size: 16, color: "666666" })
          ],
          border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: "1F4E79", space: 4 } }
        })]
      })
    },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [
            new TextRun({ text: "Stranica ", size: 16 }),
            new TextRun({ children: [PageNumber.CURRENT], size: 16 }),
            new TextRun({ text: " / ", size: 16 }),
            new TextRun({ children: [PageNumber.TOTAL_PAGES], size: 16 }),
            new TextRun({ text: "  •  Načelo: Svaki uzorak koji ne može na sud — nije uzorak, nego trošak.", size: 16, italics: true, color: "666666" })
          ]
        })]
      })
    },
    children: [
      // Title
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { after: 80 },
        children: [new TextRun({ text: "PROTOKOL UZORKOVANJA", size: 36, bold: true, color: "1F4E79" })]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { after: 200 },
        children: [new TextRun({ text: "SLOVENSKI TERENSKI TIM — verzija 2.1 (korigirano)", size: 24, color: "2E75B6" })]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { after: 300 },
        children: [new TextRun({ text: "Status: INTERNO — za tim i pravnog zastupnika. Nije za javnu objavu.", size: 18, italics: true, color: "C00000" })]
      }),

      // 1. PRAVNI OKVIR
      new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("1. PRAVNI OKVIR — ŠTO TIM MORA IMATI PRIJE POČETKA")] }),
      
      new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [
        new TextRun({ text: "Akreditacija: ", bold: true }),
        new TextRun("uzorkovatelj s iskustvom po ISO/IEC 17025 praksi (analitički kemičar); uz svaki uzorak ime i potpis.")
      ]}),
      new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [
        new TextRun({ text: "Lanac dokaza (Chain of Custody): ", bold: true }),
        new TextRun("obrazac po uzorku — datum, vrijeme, GPS, metoda, foto uzorka i mjesta, broj uzorka, vrsta analize, potpis uzorkovatelja + potpis svjedoka.")
      ]}),
      new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [
        new TextRun({ text: "Laboratorij: ", bold: true }),
        new TextRun("unaprijed ugovoren "),
        new TextRun({ text: "akreditirani", bold: true }),
        new TextRun(" laboratorij (npr. Institut Jožef Stefan Ljubljana / IRB Zagreb / drugi EU s ISO 17025). "),
        new TextRun({ text: "Prije terena obavezno provjeriti točan opseg akreditacije", bold: true }),
        new TextRun(" za tražene analize (VOC, teški metali, halogenidi, PCDD/F, eventualno Sr-90). Uzorak izvan opsega akreditacije = oboriv uzorak.")
      ]}),
      new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [
        new TextRun({ text: "Pravni svjedok: ", bold: true }),
        new TextRun("pravnik ili predstavnik NGO-a (gdje je izvedivo) uz ekipu.")
      ]}),
      new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [
        new TextRun({ text: "Ovlaštenje/identifikacija: ", bold: true }),
        new TextRun("tim nosi ovaj protokol + osobne isprave; uzorkuje "),
        new TextRun({ text: "isključivo s javnih površina", bold: true }),
        new TextRun(" (ceste, nogostupi, zeleni pojas, obalno morsko dobro).")
      ]}),

      // 2. PONAŠANJE NA TERENU
      new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("2. PONAŠANJE NA TERENU")] }),
      
      new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [
        new TextRun({ text: "Bez sukoba. ", bold: true }),
        new TextRun("Na upit: predstaviti se, pokazati ispravu/protokol, objasniti svrhu (neovisno znanstveno uzorkovanje kvalitete zraka/vode/tla s javnih površina, čl. 4. Aarhuške konvencije). Na privatnom posjedu ne inzistirati — uzorkovati s javne površine i zabilježiti odbijenicu (to je dokaz o prikrivanju).")
      ]}),
      new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [
        new TextRun({ text: "Uzorkovanje se provodi DANJU I OTVORENO, ", bold: true }),
        new TextRun("uz foto/video zapisnik. Izbjegavanje nadzora (noćno/rano jutro) ruši vjerodostojnost dokaza. Sigurnosni razlozi rješavaju se izborom točke, a ne mrakom.")
      ]}),
      new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [
        new TextRun({ text: "Nema „cover storyja\". ", bold: true }),
        new TextRun("Na pitanje odgovara se istinom: „provodimo neovisno znanstveno uzorkovanje za potrebe građanske dokazne građe; metodologija i laboratorij su poznati i bit će javno objavljeni s rezultatima\".")
      ]}),
      new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [
        new TextRun({ text: "Snimanje: ", bold: true }),
        new TextRun("cijeli postupak na kameru/mobitel (javni prostor). Snimiti i svaku opstrukciju/prijetnju + ime, vrijeme, mjesto. Svaka fotka → odmah hash (certutil / SHA-256 alat) i upis u manifest dana. Snimke odmah uploadati na privatni cloud s vremenskim pečatom.")
      ]}),
      new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [
        new TextRun({ text: "Zaštita: ", bold: true }),
        new TextRun("FFP2/FFP3 maske, rukavice, zaštitna odijela, naočale.")
      ]}),
      new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [
        new TextRun({ text: "Koordinacija: ", bold: true }),
        new TextRun("lokalni vodič "),
        new TextRun({ text: "ne sudjeluje u samom uzorkovanju", bold: true }),
        new TextRun(" (zbog prigovora pristranosti). Svi zapisnici istog dana koordinatorici i nositelju dosjea.")
      ]}),

      // 3. LOKACIJE
      new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("3. LOKACIJE I MATRICA UZORAKA")] }),

      new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun("3.1 PAZIN — Sekundar usluge (Industrijska 17) — izvan ograde")] }),
      new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [new TextRun("Voda: 3 točke (uzvodno kontrola / izlaz iz dvorišta / nizvodno 100 m).")] }),
      new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [new TextRun("Tlo: rub dvorišta, 0–10 cm i 10–30 cm (samo javna površina).")] }),
      new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [new TextRun("Zrak: pasivni uzorkivači VOC + teški metali na javnom stupu uz ogradu; alternativno prašina s krovova/lišća u blizini.")] }),
      new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [new TextRun("Kamioni u zastoju: bris vanjske strane (blato/prašina) — indikacija, ne dokaz sastava tereta.")] }),
      new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [new TextRun({ text: "Ulazak u krug: ne pokušavati. ", bold: true }), new TextRun("Katastar + javni putevi. Paralelno: zahtjev DIRH-u da službeno uzme uzorke.")] }),

      new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun("3.2 KOROMAČNO — kružni tok, silos, Raški zaljev")] }),
      new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [new TextRun("Morska voda: 3 točke (obala ispred tvornice / 100 m od obale / ulaz u zaljev = kontrola), dubine 0,5 m i 2 m. Ako je moguće — i sediment na istoj točki.")] }),
      new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [new TextRun("Sediment mora (ako dohvatljiv) — teški metali + organski zagađivači.")] }),
      new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [new TextRun("Slatka voda: potoci koji se ulijevaju u more.")] }),
      new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [new TextRun("Krški izvori u okolici (Brovinje, Trget) — ako su dostupni s javnog dobra.")] }),
      new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [new TextRun("Prašina s krovova/lišća — teški metali, halogenidi.")] }),
      new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [new TextRun("Obalni pojas = javno dobro; parkiranje na javnom parkiralištu, pristup pješice.")] }),

      new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun("3.3 LABIN / BRŠICA — tranzitna ruta")] }),
      new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [new TextRun("Tlo/prašina s ruba ceste i jaraka na mjestima stajanja kamiona.")] }),
      new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [new TextRun("Voda iz oborinskih kanala uz cestu.")] }),
      new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [new TextRun("Zrak: pasivni uzorkivači na bankinama (VOC).")] }),
      new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [new TextRun("Carinski prostor: ne ulaziti bez dozvole; uzorkovanje s javnog parkirališta ako je dostupno.")] }),
      new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [new TextRun({ text: "Uz blokade: ", bold: true }), new TextRun("koordinirati s mještanima za pristup rubu ceste; tim je promatrač/uzorkovatelj, ne prosvjednik.")] }),

      // 4. AKO ULAZ NIJE DOZVOLJEN
      new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("4. AKO ULAZ/PRISTUP NIJE DOZVOLJEN")] }),
      new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [new TextRun("Pristojno se povući; uzorkovati s javne površine.")] }),
      new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [new TextRun("Zabilježiti opstrukciju: video, ime osobe, vrijeme, mjesto → prijava pravnom zastupniku naknadno.")] }),
      new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [new TextRun("Ako tim bude zadržan: odmah kontaktirati koordinatoricu i pravni kontakt; ne raspravljati na licu mjesta.")] }),

      // 5. PAKIRANJE
      new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("5. PAKIRANJE I SLANJE UZORAKA")] }),
      new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [new TextRun("Sterilne posude, hermetički zatvorene, etiketa + Chain of Custody obrazac.")] }),
      new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [new TextRun("Kurir (DHL/slično) izravno u laboratorij, s povratnicom; kopija dokumentacije e-mailom istovremeno koordinatorici i nositelju dosjea.")] }),
      new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: [new TextRun("Svaki uzorak = red u MANIFEST-UZORCI (broj uzorka, hash foto mjesta, laboratorij, datum slanja).")] }),

      // 6. ZAKLJUČAK
      new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("6. ZAKLJUČAK")] }),
      new Paragraph({
        spacing: { before: 100 },
        children: [new TextRun({ text: "Tim radi hladno, danju, javno i s papirom u ruci. ", bold: true }),
          new TextRun("Dokaz koji drži u Strasbourgu i pred OLAF-om nije onaj koji je netko „uspio uzeti neviđen\" — nego onaj za koji svatko može provjeriti tko ga je, kada, gdje i kako uzeo, i koji laboratorij ga je, s kojom akreditacijom, analizirao.")]
      }),
      new Paragraph({
        spacing: { before: 200 },
        alignment: AlignmentType.CENTER,
        children: [new TextRun({ text: "— Kraj protokola v2.1 —", size: 18, italics: true, color: "666666" })]
      }),
    ]
  }]
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync("/home/workdir/artifacts/Protokol_Uzorkovanja_v2.1_CISTO.docx", buffer);
  console.log("Protokol created successfully");
});
