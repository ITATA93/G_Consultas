# websys.Document

**Schema:** websys
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| DataId | varchar |  |  | SI | Id of the foreign data global (eg ^websys.Document... |
| DataType | varchar |  |  | SI | Name of the foreign data global (eg TIF) |
| docData | longvarbinary |  |  | SI | is now a transient field - retrieved from stored w... |
| docDataChar | longvarchar |  |  | SI | equivalent data as field docData, except used for ... |
| docType | varchar |  |  | SI | extension of attachment |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*