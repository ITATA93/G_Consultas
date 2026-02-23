# questionnaire.QTCEIDCTQQ29

> Informe de Derivación Centros de Tratamiento : Caracterización del Consumo

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Informe de Derivación Centros de Tratamiento : Caracterización del Consumo

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q29Q1 | varchar |  |  | SI | Categoria |
| Q29Q2 | varchar |  |  | SI | Sustancia |
| Q29Q3 | varchar |  |  | SI | Frecuencia |
| Q29Q4 | varchar |  |  | SI | Edad de Inicio |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*