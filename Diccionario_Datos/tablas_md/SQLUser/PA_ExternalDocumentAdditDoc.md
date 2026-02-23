# SQLUser.PA_ExternalDocumentAdditDoc

**Schema:** SQLUser
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Extensión de datos adicionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADDIT_ParRef | bigint | PK |  | NO | PAExternalDocument Parent Reference |
| ADDIT_Childsub | double |  |  | NO | Childsub |
| ADDIT_Document_DR | bigint |  | FK | SI | Des Ref websys.Document |
| ADDIT_FileName | varchar |  |  | SI | File Name |
| ADDIT_Path | varchar |  |  | SI | Path |
| ADDIT_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*