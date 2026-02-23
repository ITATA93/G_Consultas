# SQLUser.LB_InstrumentEventAttachment

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBIEATT_ParRef | bigint | PK |  | NO | Parent Instrument Event DR |
| ChildQ159DR | - |  |  | SI | Child Reference: Agudeza Visual (Espec.) |
| LBIEATT_Comments | varchar |  |  | SI | File comments |
| LBIEATT_Document_DR | bigint |  | FK | SI | Link to the websys.document |
| LBIEATT_FileName | varchar |  |  | SI | File name |
| LBIEATT_FileType | varchar |  |  | SI | Type of the document file JPG, BMP, SVG, etc... |
| LBIEATT_RowID | varchar |  |  | NO | - |
| Q113Q1 | - |  |  | SI | Localización anatómica |
| Q113Q2 | - |  |  | SI | Sensibilidad táctil |
| Q113Q3 | - |  |  | SI | Sensibilidad térmica |
| Q113Q4 | - |  |  | SI | Sensibilidad nociceptiva |
| Q113Q5 | - |  |  | SI | Propiocepción |
| Q113Q6 | - |  |  | SI | Sensibilidad vibratoria |
| Q113Q7 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*