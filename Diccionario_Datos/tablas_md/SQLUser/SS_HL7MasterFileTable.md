# SQLUser.SS_HL7MasterFileTable

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HL7MFT_ParRef | varchar | PK |  | NO | SS_HL7MasterFileMsg Parent Reference |
| HL7MFT_ExternalTable | varchar |  |  | NO | Updated External Table |
| HL7MFT_RowId | varchar |  |  | NO | - |
| HL7MFT_Table | varchar |  |  | SI | TrakCare table |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*