# questionnaire.QTCECOLPOQQ07

> Colposcopía : COLPOSCOPÍA ANORMAL

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Colposcopía : COLPOSCOPÍA ANORMAL

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q07Q1 | varchar |  |  | SI | Imágenes atípicas |
| Q07Q2 | varchar |  |  | SI | Cambios |
| Q07Q3 | varchar |  |  | SI | Topografía de la imagen cervical |
| Q07Q4 | varchar |  |  | SI | Comentarios |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*