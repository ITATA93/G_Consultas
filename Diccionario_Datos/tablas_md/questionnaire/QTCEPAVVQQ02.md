# questionnaire.QTCEPAVVQQ02

> Vía Venosa : Via Venosa Central

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Vía Venosa : Via Venosa Central

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q02Q1 | varchar |  |  | SI | Diámetro (#) |
| Q02Q2 | varchar |  |  | SI | Ubicación |
| Q02Q3 | varchar |  |  | SI | Complejidad |
| Q02Q4 | varchar |  |  | SI | Observación |
| Q02Q5 | varchar |  |  | SI | Lateralidad |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*