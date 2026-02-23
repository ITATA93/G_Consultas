# questionnaire.QTCEPAVVQQ01

> Vía Venosa : Via Venosa Periférica

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Vía Venosa : Via Venosa Periférica

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q01Q1 | varchar |  |  | SI | Diámetro (#) |
| Q01Q2 | varchar |  |  | SI | Ubicación |
| Q01Q3 | varchar |  |  | SI | Complejidad |
| Q01Q4 | varchar |  |  | SI | Observación |
| Q01Q5 | varchar |  |  | SI | Lateralidad |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*