# questionnaire.QCLXXINPAQUQQ26

> Ingreso de Paciente Quemado : Localización y Profundidad de la/las quemaduras

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ingreso de Paciente Quemado : Localización y Profundidad de la/las quemaduras

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q26Q1 | varchar |  |  | SI | Localización |
| Q26Q2 | varchar |  |  | SI | Otra parte del cuerpo |
| Q26Q3 | varchar |  |  | SI | Clasificación Benaim |
| Q26Q4 | varchar |  |  | SI | Otra Clasificación |
| Q26Q5 | varchar |  |  | SI | Índice de Gravedad |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*