# Tools_DrugUpload.SchemaItems

**Schema:** Tools_DrugUpload
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| SchemaCode | varchar |  |  | NO | Code of Schema to be used |
| SchemaGroupCode | varchar |  |  | NO | Code of Group in this Schema to be linked to |
| TrakCode | varchar |  |  | NO | Code depending on Type |
| TrakType | varchar |  |  | NO | TrakType that declaires which Type, can be PCK,ING... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*