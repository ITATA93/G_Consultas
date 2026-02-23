# questionnaire.QTCEINGUPCQQ64

> INGRESO UNIDAD DE PACIENTE CRÍTICO : Abdomen

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* INGRESO UNIDAD DE PACIENTE CRÍTICO : Abdomen

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q64Q1 | varchar |  |  | SI | Palpación |
| Q64Q2 | varchar |  |  | SI | Percusión |
| Q64Q3 | varchar |  |  | SI | Auscultación |
| Q64Q4 | varchar |  |  | SI | Localización |
| Q64Q5 | varchar |  |  | SI | Lateralidad |
| Q64Q6 | varchar |  |  | SI | Comentario |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*