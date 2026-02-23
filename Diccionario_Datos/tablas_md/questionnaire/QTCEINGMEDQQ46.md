# questionnaire.QTCEINGMEDQQ46

> Ingreso Medicina Interna : Lesiones cutáneas

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ingreso Medicina Interna : Lesiones cutáneas

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q46Q1 | varchar |  |  | SI | Tipo de lesión |
| Q46Q2 | varchar |  |  | SI | Consistencia |
| Q46Q3 | varchar |  |  | SI | Cantidad |
| Q46Q4 | varchar |  |  | SI | Tamaño |
| Q46Q5 | varchar |  |  | SI | Ubicación |
| Q46Q6 | varchar |  |  | SI | Localización topográfica |
| Q46Q7 | varchar |  |  | SI | Comentario |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*