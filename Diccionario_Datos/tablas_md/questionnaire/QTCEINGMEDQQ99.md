# questionnaire.QTCEINGMEDQQ99

> Ingreso Medicina Interna : Abdomen

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ingreso Medicina Interna : Abdomen

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q99Q1 | varchar |  |  | SI | Palpación |
| Q99Q2 | varchar |  |  | SI | Percusión |
| Q99Q3 | varchar |  |  | SI | Auscultación |
| Q99Q4 | varchar |  |  | SI | Localización |
| Q99Q5 | varchar |  |  | SI | Lateralidad |
| Q99Q6 | varchar |  |  | SI | Comentarios |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*