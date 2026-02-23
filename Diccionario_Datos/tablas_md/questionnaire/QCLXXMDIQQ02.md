# questionnaire.QCLXXMDIQQ02

> Mantención Dispositivos Invasivos : Catéteres Venosos

**Schema:** questionnaire
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Mantención Dispositivos Invasivos : Catéteres Venosos

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q02Q1 | varchar |  |  | SI | Tipo Catéteres |
| Q02Q10 | varchar |  |  | SI | ¿Es necesario el DI? |
| Q02Q2 | varchar |  |  | SI | Actividad |
| Q02Q3 | varchar |  |  | SI | Ubicación |
| Q02Q4 | varchar |  |  | SI | Tamaño Catéter |
| Q02Q5 | varchar |  |  | SI | N° Días de Catéter |
| Q02Q6 | varchar |  |  | SI | Permeabilidad |
| Q02Q7 | varchar |  |  | SI | Características Sitio de Inserción |
| Q02Q8 | varchar |  |  | SI | Estado de Cobertura |
| Q02Q9 | varchar |  |  | SI | Solución Antiséptica |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*