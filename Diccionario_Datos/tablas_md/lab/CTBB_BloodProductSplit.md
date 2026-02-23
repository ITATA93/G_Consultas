# lab.CTBB_BloodProductSplit

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo Banco de Sangre**. Configuración de hemoterapia.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BBBPS_ParRef | varchar | PK |  | NO | CTBB_BloodProduct Parent Reference |
| BBBPS_Description | varchar |  |  | SI | Description |
| BBBPS_Products | varchar |  |  | SI | Products |
| BBBPS_RowID | varchar |  |  | NO | - |
| BBBPS_Sequence | numeric |  |  | NO | Sequence |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*