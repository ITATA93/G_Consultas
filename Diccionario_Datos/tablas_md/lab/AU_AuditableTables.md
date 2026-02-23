# lab.AU_AuditableTables

**Schema:** lab
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Auditoría de modificaciones.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AUT_RowID | double | PK |  | NO | - |
| AUT_Description | varchar |  |  | SI | Description |
| AUT_EnableDeletion | varchar |  |  | SI | Enable Deletion (Trak only) |
| AUT_EnableDeletionAfterLive | varchar |  |  | SI | Enable Deletion After Live |
| AUT_MasterTable_DR | double |  | FK | SI | Master Table |
| AUT_TableID | double |  |  | NO | Table ID |
| AUT_xxx1 | varchar |  |  | SI | Check Update |
| AUT_xxx2 | varchar |  |  | SI | Check Delete |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*