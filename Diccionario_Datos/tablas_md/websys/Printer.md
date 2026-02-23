# websys.Printer

> Printer Definition

**Schema:** websys
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Printer Definition

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| BatchPrint | bit |  |  | SI | - |
| Code | varchar |  |  | SI | Code is used to unqiuely identify a printer |
| Description | varchar |  |  | SI | Description of the Printer.<br>
e.g. ZEBRA Bar Co... |
| Device | varchar |  |  | SI | Printer device.<br>
This should be the sharename ... |
| LocalPrinter | bit |  |  | SI | Flag to indicate if printer is local |
| MFDPassUserName | bit |  |  | SI | Flag to indicate if printer is MFD that requires u... |
| PostScript | bit |  |  | SI | Flag to indicate if printer support postscript pri... |
| PrinterDisabled | bit |  |  | SI | Log 45134 - AI - 16-11-2005 : Printer Disabled che... |
| PrinterGroup | bigint |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*