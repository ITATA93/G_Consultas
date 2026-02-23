# web_Msg.LBC_SpecimenGroupItem

**Schema:** web_Msg
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBCSPGI_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCSPGI_ParRef | bigint |  |  | SI | Parent SpecimenGroup DR |
| LBCSPGI_RowID | varchar |  |  | SI | - |
| LBCSPGI_Specimen_DR | bigint |  | FK | SI | Specimen DR |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*