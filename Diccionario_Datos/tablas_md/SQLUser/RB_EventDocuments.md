# SQLUser.RB_EventDocuments

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SD_ParRef | bigint | PK |  | NO | RB_Event Parent Reference |
| SD_Childsub | double |  |  | NO | Childsub |
| SD_Desc | varchar |  |  | SI | Description |
| SD_DocumentType_DR | bigint |  | FK | SI | Des Ref DocumentType |
| SD_File | varchar |  |  | SI | File |
| SD_RowId | varchar |  |  | NO | - |
| SD_websysDocument | bigint |  |  | SI | websysDocument |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*